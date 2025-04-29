<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ojp="http://www.vdv.de/ojp" xmlns:siri="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vdv.de/ojp">
	<xsl:output method="xml" encoding="UTF-8" indent="yes"/>
	<xsl:template match="ojp:TravelClass">
		<xsl:choose>
			<xsl:when test=". = 'first'">
				<ojp:FareClass>firstClass</ojp:FareClass>
			</xsl:when>
			<xsl:when test=". = 'second'">
				<ojp:FareClass>secondClass</ojp:FareClass>
			</xsl:when>
			<xsl:otherwise>
				<ojp:FareClass>unknown</ojp:FareClass>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<xsl:template match="ojp:OJPFareDelivery">
		<OJP xmlns="http://www.vdv.de/ojp" xmlns:siri="http://www.siri.org.uk/siri" version="2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vdv.de/ojp">
			<OJPResponse>
				<siri:ServiceDelivery>
					<xsl:copy-of select="//siri:ResponseTimestamp"/>
					<OJPFareDelivery>
						<xsl:copy-of select="//siri:ResponseTimestamp"/>
						<xsl:apply-templates select="//ojp:FareResult"/>
					</OJPFareDelivery>
				</siri:ServiceDelivery>
			</OJPResponse>
		</OJP>
	</xsl:template>
	<xsl:template match="ojp:FareResult">
		<ojp:FareResult>
			<xsl:element name="ojp:Id">
				<xsl:value-of select="//ojp:ResultId"/>
			</xsl:element>
			<xsl:apply-templates select="ojp:TripFareResult"/>
		</ojp:FareResult>
	</xsl:template>
	<xsl:template match="ojp:TripFareResult">
		<ojp:TripFareResult>
			<xsl:element name="ojp:FromLegIdRef">
				<xsl:value-of select="ojp:FromTripLegIdRef"/>
			</xsl:element>
			<xsl:element name="ojp:ToLegIdRef">
				<xsl:value-of select="ojp:ToTripLegIdRef"/>
			</xsl:element>
			<xsl:apply-templates select="ojp:FareProduct"/>
		</ojp:TripFareResult>
	</xsl:template>
	<xsl:template match="ojp:FareProduct">
		<ojp:FareProduct>
			<xsl:element name="ojp:FareProductId">
				<xsl:value-of select="ojp:FareProductId"/>
			</xsl:element>
			<xsl:element name="ojp:FareProductName">
				<xsl:value-of select="ojp:FareProductName"/>
			</xsl:element>
			<xsl:element name="ojp:FareAuthorityRef">
				<xsl:value-of select="ojp:FareAuthorityRef"/>
			</xsl:element>
			<xsl:element name="ojp:FareAuthorityText">
				<xsl:value-of select="ojp:FareAuthorityText"/>
			</xsl:element>
			<xsl:element name="ojp:Price">
				<xsl:value-of select="ojp:Price"/>
			</xsl:element>
			<xsl:element name="ojp:NetPrice">
				<xsl:value-of select="ojp:NetPrice"/>
			</xsl:element>
			<xsl:element name="ojp:Currency">
				<xsl:value-of select="ojp:Currency"/>
			</xsl:element>
			<xsl:element name="ojp:VatRate">
				<xsl:value-of select="ojp:VatRate"/>
			</xsl:element>
			<xsl:apply-templates select="ojp:TravelClass"/>
		</ojp:FareProduct>
	</xsl:template>
</xsl:stylesheet>