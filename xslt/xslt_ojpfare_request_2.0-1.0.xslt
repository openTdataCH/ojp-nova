<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ojp="http://www.vdv.de/ojp" xmlns:siri="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.siri.org.uk/siri file:///C:/Users/ue71603/MG_Daten/github/OJP4/OJP.xsd">
	<xsl:output method="xml" encoding="UTF-8" indent="yes"/>
	<!-- function to copy stuff, when the field exists -->
	<xsl:template name="copyElement">
		<xsl:param name="input"/>
		<xsl:param name="output"/>
		<xsl:if test="$input">
			<xsl:element name="{$output}">
				<xsl:value-of select="$input"/>
			</xsl:element>
		</xsl:if>
	</xsl:template>
	<!-- root -->
	<xsl:template match="ojp:OJP">
		<OJP xmlns:ojp="http://www.vdv.de/ojp" xmlns="http://www.siri.org.uk/siri" version="1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vdv.de/ojp">
			<OJPRequest>
				<ServiceRequest>
					<xsl:element name="RequestTimestamp">
						<xsl:value-of select="//siri:RequestTimestamp"/>
					</xsl:element>
					<xsl:element name="RequestorRef">
						<xsl:value-of select="//siri:RequestorRef"/>
					</xsl:element>
					<xsl:apply-templates select="//ojp:OJPFareRequest"/>
				</ServiceRequest>
			</OJPRequest>
		</OJP>
	</xsl:template>
	<xsl:template match="ojp:OJPFareRequest">
		<ojp:OJPFareRequest>
			<xsl:element name="siri:RequestTimestamp">
				<xsl:value-of select="siri:RequestTimestamp"/>
			</xsl:element>
			<xsl:apply-templates select="//ojp:TripFareRequest"/>
			<xsl:apply-templates select="ojp:Params"/>
		</ojp:OJPFareRequest>
	</xsl:template>
	<xsl:template match="ojp:TripFareRequest">
		<ojp:TripFareRequest>
			<xsl:apply-templates select="ojp:Trip"/>
		</ojp:TripFareRequest>
	</xsl:template>
	<xsl:template match="ojp:Trip">
		<ojp:Trip>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:Id"/>
				<xsl:with-param name="output" select="'ojp:TripId'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:Duration"/>
				<xsl:with-param name="output" select="'ojp:Duration'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:StartTime"/>
				<xsl:with-param name="output" select="'ojp:StartTime'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:EndTime"/>
				<xsl:with-param name="output" select="'ojp:EndTime'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:Transfers"/>
				<xsl:with-param name="output" select="'ojp:Transfers'"/>
			</xsl:call-template>
			<xsl:apply-templates select="ojp:Leg"/>
		</ojp:Trip>
	</xsl:template>
	<xsl:template match="ojp:Leg">
		<ojp:TripLeg>
			<ojp:LegId>
				<xsl:value-of select="ojp:Id"/>
			</ojp:LegId>
			<xsl:apply-templates select="ojp:ContinuousLeg"/>
			<xsl:apply-templates select="ojp:TransferLeg"/>
			<xsl:apply-templates select="ojp:TimedLeg"/>
		</ojp:TripLeg>
	</xsl:template>
	<xsl:template match="ojp:ContinuousLeg">
		<ojp:ContinuousLeg>
			<xsl:apply-templates select="ojp:LegStart"/>
			<xsl:apply-templates select="ojp:LegEnd"/>
			<xsl:apply-templates select="ojp:Service"/>
			<!-- not defined are
                <ojp:TimeWindowStart>2025-04-28T12:05:00Z</ojp:TimeWindowStart>
                <ojp:TimeWindowEnd>2025-04-28T12:22:00Z</ojp:TimeWindowEnd>
                <ojp:Duration>PT6M</ojp:Duration> -->
		</ojp:ContinuousLeg>
	</xsl:template>
	<xsl:template match="ojp:LegStart">
		<ojp:LegStart>
			<!-- only GepoPosition allowed -->
			<xsl:apply-templates select="ojp:GeoPosition"/>
			<xsl:apply-templates select="ojp:LocationName"/>
		</ojp:LegStart>
	</xsl:template>
	<xsl:template match="ojp:LegEnd">
		<ojp:LegEnd>
			<xsl:apply-templates select="ojp:GeoPosition"/>
			<xsl:apply-templates select="ojp:LocationName"/>
		</ojp:LegEnd>
	</xsl:template>
	<xsl:template match="ojp:GeoPosition">
		<ojp:GeoPosition>
			<Longitude>
				<xsl:value-of select="siri:Longitude"/>
			</Longitude>
			<Latitude>
				<xsl:value-of select="siri:Latitude"/>
			</Latitude>
			<!-- we only support Longitude/Latitude here -->
		</ojp:GeoPosition>
	</xsl:template>
	<xsl:template match="ojp:LocationName">
		<ojp:LocationName>
			<ojp:Text xml:lang="{ojp:Text/@xml:lang}">
				<xsl:value-of select="ojp:Text"/>
			</ojp:Text>
		</ojp:LocationName>
	</xsl:template>
	<xsl:template match="ojp:StopPointName">
		<ojp:StopPointName>
			<ojp:Text xml:lang="{ojp:Text/@xml:lang}">
				<xsl:value-of select="ojp:Text"/>
			</ojp:Text>
		</ojp:StopPointName>
	</xsl:template>
	<xsl:template match="ojp:Name">
		<ojp:Name>
			<ojp:Text xml:lang="{ojp:Text/@xml:lang}">
				<xsl:value-of select="ojp:Text"/>
			</ojp:Text>
		</ojp:Name>
	</xsl:template>
	<xsl:template match="ojp:PublishedServiceName">
		<ojp:PublishedLineName>
			<ojp:Text xml:lang="{ojp:Text/@xml:lang}">
				<xsl:value-of select="ojp:Text"/>
			</ojp:Text>
		</ojp:PublishedLineName>
	</xsl:template>
	<xsl:template match="ojp:NameSuffix">
		<ojp:NameSuffix>
			<ojp:Text xml:lang="{ojp:Text/@xml:lang}">
				<xsl:value-of select="ojp:Text"/>
			</ojp:Text>
		</ojp:NameSuffix>
	</xsl:template>
	<xsl:template match="ojp:TimedLeg">
		<ojp:TimedLeg>
			<xsl:apply-templates select="ojp:LegBoard"/>
			<xsl:apply-templates select="ojp:LegIntermediates"/>
			<xsl:apply-templates select="ojp:LegAlight"/>
			<xsl:apply-templates select="ojp:Service"/>
			<xsl:apply-templates select="ojp:Extension"/>
		</ojp:TimedLeg>
	</xsl:template>
	<xsl:template match="ojp:LegIntermediates">
		<ojp:LegIntermediates>
			<!-- we only support StopPointRef for now -->
			<siri:StopPointRef>
				<xsl:value-of select="siri:StopPointRef"/>
			</siri:StopPointRef>
			<xsl:apply-templates select="ojp:StopPointName"/>
			<xsl:apply-templates select="ojp:NameSuffix"/>
			<xsl:apply-templates select="ojp:ServiceArrival"/>
			<xsl:apply-templates select="ojp:ServiceDeparture"/>
			<ojp:Order>
				<xsl:value-of select="ojp:Order"/>
			</ojp:Order>
		</ojp:LegIntermediates>
	</xsl:template>
	<xsl:template match="ojp:LegAlight">
		<ojp:LegAlight>
			<!-- we only support StopPointRef for now -->
			<siri:StopPointRef>
				<xsl:value-of select="siri:StopPointRef"/>
			</siri:StopPointRef>
			<xsl:apply-templates select="ojp:StopPointName"/>
			<xsl:apply-templates select="ojp:NameSuffix"/>
			<xsl:apply-templates select="ojp:ServiceArrival"/>
			<ojp:Order>
				<xsl:value-of select="ojp:Order"/>
			</ojp:Order>
		</ojp:LegAlight>
	</xsl:template>
	<xsl:template match="ojp:LegBoard">
		<ojp:LegBoard>
			<!-- we only support StopPointRef for now -->
			<siri:StopPointRef>
				<xsl:value-of select="siri:StopPointRef"/>
			</siri:StopPointRef>
			<xsl:apply-templates select="ojp:StopPointName"/>
			<xsl:apply-templates select="ojp:NameSuffix"/>
			<xsl:apply-templates select="ojp:ServiceDeparture"/>
			<ojp:Order>
				<xsl:value-of select="ojp:Order"/>
			</ojp:Order>
		</ojp:LegBoard>
	</xsl:template>
	<xsl:template match="ojp:ServiceDeparture">
		<ojp:ServiceDeparture>
			<ojp:TimetabledTime>
				<xsl:value-of select="ojp:TimetabledTime"/>
			</ojp:TimetabledTime>
			<!-- Ignore all other stuff -->
		</ojp:ServiceDeparture>
	</xsl:template>
	<xsl:template match="ojp:ServiceArrival">
		<ojp:ServiceArrival>
			<ojp:TimetabledTime>
				<xsl:value-of select="ojp:TimetabledTime"/>
			</ojp:TimetabledTime>
			<!-- Ignore all other stuff -->
		</ojp:ServiceArrival>
	</xsl:template>
	<xsl:template match="ojp:Mode">
		<ojp:Mode>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:PtMode"/>
				<xsl:with-param name="output" select="'ojp:PtMode'"/>
			</xsl:call-template>
			<xsl:apply-templates select="ojp:Name"/>
		</ojp:Mode>
	</xsl:template>
	<xsl:template match="ojp:Attribute">
		<ojp:Attribute>
			<xsl:apply-templates select="ojp:Text"/>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:Code"/>
				<xsl:with-param name="output" select="'ojp:Code'"/>
			</xsl:call-template>
		</ojp:Attribute>
	</xsl:template>
	<xsl:template match="Extension">
		<ojp:Extension>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:TransportTypeName"/>
				<xsl:with-param name="output" select="'ojp:TransportTypeName'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:PublishedJourneyNumber"/>
				<xsl:with-param name="output" select="'ojp:PublishedJourneyNumber'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:OperatorName"/>
				<xsl:with-param name="output" select="'ojp:OperatorName'"/>
			</xsl:call-template>
		</ojp:Extension>
	</xsl:template>
	<xsl:template match="ojp:TransferLeg">
		<ojp:TransferLeg>
			<xsl:apply-templates select="ojp:Service"/>
			<!-- ignore the rest -->
		</ojp:TransferLeg>
	</xsl:template>
	<xsl:template match="ojp:Service">
		<ojp:Service>
			<!-- for TransferLeg and ContinuousLeg -->
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:IndividualMode"/>
				<xsl:with-param name="output" select="'ojp:IndividualMode'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:OperatingDayRef"/>
				<xsl:with-param name="output" select="'ojp:OperatingDayRef'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:JourneyRef"/>
				<xsl:with-param name="output" select="'ojp:JourneyRef'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="siri:LineRef"/>
				<xsl:with-param name="output" select="'siri:LineRef'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="siri:DirectionRef"/>
				<xsl:with-param name="output" select="'siri:DirectionRef'"/>
			</xsl:call-template>
			<xsl:apply-templates select="ojp:Mode"/>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="ojp:PublishedLineName"/>
				<xsl:with-param name="output" select="'ojp:PublishedLineName'"/>
			</xsl:call-template>
			<xsl:call-template name="copyElement">
				<xsl:with-param name="input" select="siri:OperatorRef"/>
				<xsl:with-param name="output" select="'siri:OperatorRef'"/>
			</xsl:call-template>
			<xsl:apply-templates select="ojp:PublishedServiceName"/>
			<xsl:apply-templates select="ojp:Attribute"/>
		</ojp:Service>
	</xsl:template>
	<xsl:template match="ojp:Params">
		<ojp:Params>
			<ojp:FareAuthorityFilter>
				<xsl:value-of select="ojp:FareAuthorityFilter"/>
			</ojp:FareAuthorityFilter>
			<ojp:PassengerCategory>
				<xsl:value-of select="ojp:PassengerCategory"/>
			</ojp:PassengerCategory>
			<ojp:TravelClass>secondClass</ojp:TravelClass>
			<!--shortcut as we always do this -->
			<xsl:apply-templates select="ojp:Traveller"/>
		</ojp:Params>
	</xsl:template>
	<xsl:template match="ojp:Traveller">
		<ojp:Taveller>
			<ojp:PassengerCategory>
				<xsl:value-of select="ojp:PassengerCategory"/>
			</ojp:PassengerCategory>
			<!--Halbtax -->
		</ojp:Taveller>
	</xsl:template>
</xsl:stylesheet>
